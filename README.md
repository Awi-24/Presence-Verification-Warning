# Online Driving Lessons Time-Saver

This code is designed to save time during online lessons by warning the student when the random presence verification shows up during a class. The idea behind this code is to automate the process of watching for the verification box to appear. Additionally, staring at a computer screen for long periods of time can also cause eye strain, discomfort, and the student may go to the bathroom or get something to eat during the class. Therefore, this code not only saves time but also helps to alleviate some of the physical discomfort associated with online learning, making it a more comfortable and efficient experience for the student.

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

## Future Work
In the future, this code could be further improved to accommodate individuals with epilepsy. For instance, the code could be designed to warn individuals of potential triggers in videos or other media on their computer. This would be particularly useful for online lessons, where students are required to focus on visual stimuli for extended periods. By implementing such improvements, this code could become even more accessible and inclusive, catering to a broader range of individuals with different needs and conditions.
