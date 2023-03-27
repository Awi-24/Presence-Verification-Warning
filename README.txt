# Online Drive Lessons Time-Saver

This code is designed to save time during online drive lessons in Brazil by warning the student when the random presence verification shows up during a class. The idea behind this code is to automate the process of watching for the verification box to appear, which saves the student from having to constantly keep an eye on the screen.

## Dependencies
This code requires the following dependencies:

* cv2: OpenCV is a computer vision library used for image and video processing. This library is used for capturing and manipulating screenshots.
* numpy: NumPy is a numerical computing library used for working with arrays. This library is used to manipulate arrays of pixel data.
* time: The time module provides various time-related functions. This library is used to add a delay between each iteration of the loop to avoid overwhelming system resources.
* winsound: The winsound module provides access to the basic sound-playing machinery provided by Windows platforms. This library is used to emit an audible warning when the verification box appears.
* PIL: PIL (Python Imaging Library) is a library used for opening, manipulating, and saving many different image file formats. This library is used to capture screenshots.

## Usage
To use this code, the user must select a region of interest on their screen where the verification box appears during the online drive lesson. The code then continuously monitors this region for any changes and emits an audible warning if the verification box appears.

To select the region of interest, the code opens a window titled "Selecionar Área". The user can then press the "s" key to start selecting the region of interest. Once the region has been selected, the code automatically starts monitoring that region.

## Explanation of the Code
The code first creates a window titled "Selecionar Área" for the user to select the region of interest. It continuously captures screenshots of the screen and displays them in this window until the user presses the "s" key to start selecting the region.

Once the region of interest has been selected, the code sets up a loop to continuously monitor that region. It captures screenshots of only the selected region and converts them to grayscale. It then calculates the difference between the current frame and the previous frame.

If the difference exceeds a certain threshold, the code converts the difference to black and white and applies a threshold to it. It then counts the number of white pixels in the image and compares it to a pre-defined threshold value. If the number of white pixels exceeds the threshold, the code emits an audible warning using the winsound library.

The code then sets the current frame as the previous frame and waits for a second before capturing the next frame. This delay ensures that the code does not overwhelm system resources.