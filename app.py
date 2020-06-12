# import the necessary packages
from imutils import paths
import argparse
import cv2
threshold = 100.0
def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
fm = variance_of_laplacian(gray)
blur = False
text = "Not Blurry"
print("Not Blurry")
# if the focus measure is less than the supplied threshold,
# then the image should be considered "blurry"
if fm < threshold:
	print("Blur")
	blur = True
	text = "Blurry"
# show the image
cv2.putText(image, "{}: {:.2f}".format(text, fm), (20, 30),
    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (140, 0, 255), 2)
cv2.imshow("Image", image)
key = cv2.waitKey()