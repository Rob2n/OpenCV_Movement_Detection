import cv2
import imutils

video = cv2.VideoCapture("./video_feed.mp4")

FirstFrame = None

while 42:
	ret, frame = video.read()
	DisplayText = "Sleeping..."

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (25, 25), 100)

	if FirstFrame is None:
		FirstFrame = gray
		continue

	frameDelta = cv2.absdiff(FirstFrame, gray)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

	contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	contours = imutils.grab_contours(contours)

	for c in contours:
		if cv2.contourArea(c) < 3000:
			continue
		DisplayText = "Recording!"

	cv2.putText(frame, DisplayText, (10, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
	cv2.imshow("Big Brother", frame)

	key = cv2.waitKey(1)
	if key == ord('q'):
		exit()
