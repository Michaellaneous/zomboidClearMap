# zomboidClearMap

Following the guide [here](https://steamcommunity.com/sharedfiles/filedetails/?id=2547762158), you either want to reset a part of your map or add a new one.
To do this, you need to delete a few map and chunkfiles. Since there a quite a few, this little script does this for you. Simply enter the coordinates, point it to your save, and it will get rid of all the proper map data.

***BACKUP YOUR SAVE before you do anything. I am not responsible for you loosing 100 hours of progress.***

You need python3 in order to run this. A simple *python clearMap.py* should do the trick.

## Step One
Navigate to the [Zomboid Map Project](https://map.projectzomboid.com/)
On the left side, open the Map Coordinates tab.

![enter image description here](https://i.imgur.com/jUX4avi.png)

The first set that is important is **Coords**, the second is **Cell**.

## Step Two
Navigate to your savegame. Is it most likely located under C:\Users\\*username*\Zomboid\Saves. Find your save by navigating to the proper folders and copy the entire filepath. It should look like this:

> C:\Users\Michael\Zomboid\Saves\Sandbox\04-01-2022_03-23-17

## Step Three
Run the python script. Paste your map string, and then enter the set of coordinates.

***!! IMPORTANT !!***
 

 - The set of coordinates (Coords, not Cell) need to be trimmed as follows. i.e. you need to enter 3218 as 321 and 12860 as 1286. Just remove the last digit. I was too lazy to add that to the script. Feel free to MR this.
 -  Coordinates on the zomboid map are read from top left to bottom right. That means when selecting two points, start with the one that is up and left from your second point.

Enter all the coordinates, and the program will delete all the files. If you fuck up and do not have a backup of your save by this point, I am sorry.

If you have done everything correctly, everything in this area is now reset.
