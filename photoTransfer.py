import datetime
import shutil
import sys
import os
from os import walk

def main():
   # If two arguments weren't provided, then exit the program
   if (len(sys.argv)!= 3):
      print("Two arguments must be provided, the directory of the camera, and the directory to store the photos in")
      sys.exit(0)
      

   # Get the location of the camera's pictures and the location of where the files should be stored.
   cameraLocation = sys.argv[1]
   storageLocation = sys.argv[2]

   # Make sure that the two directories exist, if not exit the program
   if not (os.path.exists(cameraLocation)):
      print("Can't find the camera")
      sys.exit(0)

   if not (os.path.exists(storageLocation)):
      print("Can't find the directory to store files in")
      sys.exit(0)

   # Now iterate over the files in the camera and move them to the storage directory
   for (dirpath, dirnames, filenames) in walk(cameraLocation):
      for fileName in filenames:
         # Get the time that the picture was taken at
         picTime = datetime.datetime.fromtimestamp(os.path.getmtime(dirpath + "/" + fileName)).strftime("%Y-%m-%d");
         print(fileName)

         # Check to see if a directory for that file exists. 
         # If one doesn't, then create it
         if not os.path.exists(storageLocation + "/" + picTime):
            os.makedirs(storageLocation + "/" + picTime)

         # Move the picture from the camera to it's new directory
         shutil.move(dirpath + "/" + fileName, storageLocation + "/" + picTime)

if __name__ == "__main__":
   main()
