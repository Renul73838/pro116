import cv2
img = cv2.imread("solar-system.jpg")

cv2.putText(
    img,
    "Sun",
    (20,100),
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale = 1,
    color = (255,255,255)
)

cv2.putText(
    img,
    "Mercury",
    (100,300),
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale = 1,
    color = (255,255,255)
)

cv2.putText(
    img,
    "Venus",
    (200,100),
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale = 1,
    color = (255,255,255)
)

cv2.putText(
    img,
    "Earth",
    (300,300),
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale = 1,
    color = (255,255,255)
)

cv2.putText(
    img,
    "Mars",
    (380,100),
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale = 1,
    color = (255,255,255)
)

cv2.putText(
    img,
    "Jupiter",
    (500,400),
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale = 1,
    color = (255,255,255)
)

cv2.putText(
    img,
    "Saturn",
    (750,100),
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale = 1,
    color = (255,255,255)
)

cv2.putText(
    img,
    "Uranes",
    (950,300),
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale = 1,
    color = (255,255,255)
)

cv2.putText(
    img,
    "Neptune",
    (1100,100),
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale = 1,
    color = (255,255,255)
)
cv2.imshow("output",img)
cv2.waitKey(0)


