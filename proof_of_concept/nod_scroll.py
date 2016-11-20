import numpy as np


def scroll_pdf(y_avg, y_window):
    """
    Function that decides whether to scroll or not

    Input :
        y_avg : int
            Average ordinate of the centre of the eyes over time
        y_window : list
            List of ordinates of the centre of the eyes over a window of 10 frames

    Return : int
        Returns either 1,-1 or 0 representing a directive to scroll up, down or not scroll at all respectively

    """
    mean_y = np.mean(y_window)
    y_area = sum(y_window) - (len(y_window)) * y_window[0]
    threshold_y = 30
    if y_area > threshold_y:
        if mean_y >= y_avg:
            return 1
        else:
            return 0
    elif y_area < -threshold_y:
        if mean_y > y_avg:
            return 0
        else:
            return -1
    else:
        return 0


def next_page(x_avg, x_window):
    """
    Function that decides whether to turn to a new page or not

    Input :
        x_avg : int
            Average abcissa of the centre of the face over time
        x_window : list
            List of abcissae of the centre of the face over a window of 10 frames

    Return : int
        Returns either 1,-1 or 0 representing a directive to turn to the next page, previous page or not turn at all respectively

    """
    mean_x = np.mean(x_window)
    x_area = sum(x_window) - (len(x_window)) * x_window[0]
    threshold_x = 20
    threshold = 20
    if x_area > threshold_x:
        if mean_x >= x_avg:
            return 1
        else:
            return 0
    elif x_area < -threshold:
        if mean_x > x_avg:
            return 0
        else:
            return -1
    else:
        return 0

if __name__ == '__main__':
    pass
