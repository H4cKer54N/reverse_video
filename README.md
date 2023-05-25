# Reverse_video

This is a Python program that allows you to invert videos using the OpenCV library and multiprocessing. The program accepts various configuration options to customize the video inversion.

Requirements:
Python 3.x
OpenCV (installed via pip install opencv-python)
argparse (installed via pip install argparse)

Usage
The program can be run from the command line using the following format:

~~~
python invert_video.py --v <input_video> [--vo <output_video>] [--q <quality>] [--np <num_processes>]
~~~
  

Where:

<input_video> is the path and filename of the input video to be inverted.
<output_video> (optional) is the path and filename of the inverted output video. If this argument is not provided, the inverted video will be displayed in a window.
<quality> (optional) is the percentage quality of the output video. It should be an integer value between 0 and 100. By default, a quality of 100% is used.
<num_processes> (optional) is the number of processes to use for parallel processing. It should be an integer value. By default, 2 processes are used.

  Examples:
  
+ Invert a video and save the result to a file:
  
  ~~~ 
  python invert_video.py --v video.mp4 --vo inverted_video.mp4 
  ~~~

+ Invert a video and display it in a window:

  ~~~
  python invert_video.py --v video.mp4
  ~~~
  
+ Invert a video with 50% quality:

  ~~~
  python invert_video.py --v video.mp4 --q 50
  ~~~

+ Invert a video using 4 processes:

  ~~~
  python invert_video.py --v video.mp4 --np 4
  ~~~

  
## Functionality
  The program uses the OpenCV library to read the input video and process it. It utilizes the cv2.flip() method to invert each frame of the video. The processing is done in parallel using             multiprocessing, which speeds up the video inversion time.


The program displays the processing progress in the console and, if an output filename is provided, it saves the inverted video in MP4 format. If no output filename is provided, it displays the inverted video in a window.

License
This program is distributed under the MIT License. See the LICENSE file for more information.

Contributions

Contributions are welcome! If you encounter any issues or have any suggestions for improvement, feel free to open an issue or submit a pull request on the GitHub repository: [Repository](https://github.com/H4cKer54N/reverse_video).

Please note the following guidelines for contributing:

- For new features, bug fixes, or improvements, please create a new branch based on the `features` branch.
- Limit direct commits to the `main` branch. All changes to the `main` branch should be made through pull requests.
- Before merging changes into the `main` branch, ensure that your pull request has passed the necessary reviews and meets the required criteria (e.g., passing automated tests).

We appreciate your contributions and look forward to working together to improve the project. Thank you!

Contact
If you have any questions or comments, you can contact [Santiago Britos] via [snbq89@gmail.com].
