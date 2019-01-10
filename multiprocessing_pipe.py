import multiprocessing
import cv2
import numpy as np

indice = []
nparray = []
def cam_loop(pipe_parent):
    cap = cv2.VideoCapture(0)
    while True:
        _, img = cap.read()
        if img is not None:
            nparray = np.asarray(img)
            pipe_parent.send(nparray)


def show_loop(pipe_child):
    cv2.namedWindow('pepe')

    while True:
        from_queue = pipe_child.recv()
        cv2.imshow('pepe', from_queue)
        cv2.waitKey(1)


if __name__ == '__main__':
    logger = multiprocessing.log_to_stderr()
    logger.setLevel(multiprocessing.SUBDEBUG)

    pipe_parent, pipe_child = multiprocessing.Pipe()

    cam_process = multiprocessing.Process(target=cam_loop, args=(pipe_parent,))
    cam_process.start()

    show_process = multiprocessing.Process(target=show_loop, args=(pipe_child,))
    show_process.start()

    cam_process.join()
    show_loop.join()