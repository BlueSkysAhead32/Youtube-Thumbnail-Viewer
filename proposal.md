# Youtube Thumbnail Viewer (PFDA Final Project)

## Repository
https://github.com/BlueSkysAhead32/Youtube-Thumbnail-Viewer.git

## Description
This program will allow you to quickly take work-in-progress thumbnails and view them as though they were actually on 
the side bar or front page. This allows the user to quickly compare different drafts or variations to see which is best.

## Features
- Feature 1: Draft to test converter.
	- The program will open up a window. Simply inputting a .png file will output 4 different "Test" files, a dark mode and light mode
    version of both the side bar and the front page with the inserted image replacing on of the videos. The user can view each Test seperately, 
    and then choose to save the tests to a folder or delete them.
- Feature 2: Comparison mode
	- By clicking a button, the user can choose two test files from the computer. Then, a comparison file will be generated, with the two files side by side.
    This can be done with both the test files and raw thumbnails, but both must be the same.
- Feature 3: Custom Timestamp
	- The user can input the time of the video to get a more accurate view of how the thumbnail will look on the site. (because the transparent grey bar is
    bigger when the time is longer, like 2:43:24 vs. 9:51)If nothing is specified, a default number will be selected.

## Challenges
- Learning how to open the file explorer and save a file IN file explorer using python code.
- How to make buttons work for a window (and if you can even do that with pygame)
- Figureing out how to display the various errors when the User does something unexpected (.jpg instead of .png, file dimensions wrong, going to comparison mode with files already in the slots)
- How to make tkinter and pygame work together (if they can work together at all)
- The worst thing that can happen, is I pick a GUI and then midway through the project, realize it can't do what I want it to do, and then have to recode everything with the new GUI.

## Outcomes
Ideal Outcome:
- A window will open. The user will be able to input a png file, and get png test files back. They will be able to view the test files individually. They
can then save the batch of files, or instead delete the files, clearing the entire program. The User can input a video time, or they can simply leave it blank. The user can also go into a comparison tab, where they can take two images and output a combined image of the two side by side.

Minimal Viable Outcome:
- Bring the files into VS, and then the 4 test files are created in VS code itself. Not ideal, but I'll only do this if I can't get any of the additional features to work. I'm still not sure if this is possible. At the end of the day, this program makes tests files from a draft. If it can do that, I count that as a success. Maybe you don't, but I do.

## Milestones

- Week 1
  1. .png draft thumbnails output the 4 desired test files, outputted in VS for now
  2. placeholder window with layout, all working buttons

- Week 2
  1. opens a draft file from computer, displays draft file name in window, makes test files from draft (using week 1 code), displays the test file names, can 'save as' test files
  2. can view individual test files
  3. Prevent the User from doing unexpected things, like importing .jpg and such.

- Week 3
  1. make dynamic timestamp thingy
  2. make comparison mode work

- Week 4 (Final)
  1. Decide what is and isn't going into the project (I can't figure out x, so scrap)
  2. Make placeholdwer window look pleasing
  3. 