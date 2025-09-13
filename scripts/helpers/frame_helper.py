import os
import cv2
import numpy as np
from datetime import timedelta

class FrameHelper:
    def __init__(self, saving_frames_per_second=1):
        self.saving_frames_per_second = saving_frames_per_second

    def format_timedelta(td):
        """Utility function to format timedelta objects in a cool way (e.g 00:00:20.05)
        omitting microseconds and retaining milliseconds"""
        result = str(td)
        try:
            result, ms = result.split(".")
        except ValueError:
            return (result + ".00").replace(":", "-")
        ms = int(ms)
        ms = round(ms / 1e4)
        return f"{result}.{ms:02}".replace(":", "-")

    def get_saving_frames_durations(cap, saving_fps):
        """A function that returns the list of durations where to save the frames"""
        s = []
        # get the clip duration by dividing number of frames by the number of frames per second
        clip_duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)
        # use np.arange() to make floating-point steps
        for i in np.arange(0, clip_duration, 1 / saving_fps):
            s.append(i)
        return s