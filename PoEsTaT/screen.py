from PIL import ImageGrab

def getPart(dX, dY, x0=0,y0=0):
    """
    Get a portion of a screen

    :param dX: pixels of x to get
    :param dY: pixels of y to get
    :param x0: starting x, defaults to 0
    :param y0: starting y, defaults to 0
    :return: PIL image, as returned by ImageGrab.get
    """
    return ImageGrab.grab(bbox=(x0, y0, x0+dX, y0+dY))

def getSquares(x0, y0, xm, x, y, im, n=-1):
    """
    Split an image into sub parts.

    :param x0: left offset to first square
    :param y0: top offset to first square
    :param xm: delta between squares
    :param x: square width
    :param y: square height
    :param im: image to act on
    :param n: max images to split into. if not specified, splits as many as possible.
    :return: array of new images
    """

    if n < 0:
        n_best = int((im.size[0]-x0)/(xm+x))
        if n_best*(xm+x)+x0 < im.size[0]:
            n = n_best
        else:
            n = max(n_best - 1, 0)
    ima = [im.crop(box=(x0+(x+xm)*idx, y0, x0+(x+xm)*idx+x, y0+y)) for idx in range(0, n)]
    return ima
