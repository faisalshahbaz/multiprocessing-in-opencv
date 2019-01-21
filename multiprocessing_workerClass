import multiprocessing
from multiprocessing import Queue, Pool
from cam_utils import FPS, WebcamVideoStream
import cv2



def cam_loop(cap):
    return cap

def worker(input_q,output_q):
    fps = FPS().start()
    while True:
        fps.update()
        frame = input_q.get()
        output_q.put(cam_loop(frame))

    fps.stop()


if __name__ == '__main__':
    logger = multiprocessing.log_to_stderr()
    logger.setLevel(multiprocessing.SUBDEBUG)

    input_q = Queue(maxsize=10)
    output_q = Queue(maxsize=10)
    pool = Pool(5,worker, (input_q,output_q))

    video_capture =  WebcamVideoStream('crashvideo5.mp4',800,600).start()

    fps = FPS().start()

    while True:
        frame = video_capture.read()
        input_q.put(frame)
        cv2.imshow("videos",output_q.get())
        fps.update()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    fps.stop()
    pool.terminate()
    # input_q.join()
    # output_q.join()
    video_capture.stop()
    cv2.destroyAllWindows()
