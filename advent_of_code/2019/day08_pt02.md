# URL
https://adventofcode.com/2019/day/8#part2

# Description
Now you're ready to decode the image. The image is rendered by stacking the layers and aligning the pixels with the same positions in each layer. The digits indicate the color of the corresponding pixel: 0 is black, 1 is white, and 2 is transparent.

The layers are rendered with the first layer in front and the last layer in back. So, if a given position has a transparent pixel in the first and second layers, a black pixel in the third layer, and a white pixel in the fourth layer, the final image would have a black pixel at that position.

For example, given an image 2 pixels wide and 2 pixels tall, the image data 0222112222120000 corresponds to the following image layers:
```
Layer 1: 02
         22

Layer 2: 11
         22

Layer 3: 22
         12

Layer 4: 00
         00
```
Then, the full image can be found by determining the top visible pixel in each position:
```
    The top-left pixel is black because the top layer is 0.
    The top-right pixel is white because the top layer is 2 (transparent), but the second layer is 1.
    The bottom-left pixel is white because the top two layers are 2, but the third layer is 1.
    The bottom-right pixel is black because the only visible pixel in that position is 0 (from layer 4).
```
So, the final image looks like this:
```
01
10
```
What message is produced after decoding your image?

# Method of Solve
- The Part 02 of this challenge can be solved as follows:
- The Python version is as follows:
```
WIDTH = 25
HEIGHT = 6
SIZE = WIDTH * HEIGHT

with open("input08", "r") as f:
	data = f.read().strip()

layers = [
	data[i:i + SIZE]
	for i in range(0, len(data), SIZE)
]

image = ["2"] * SIZE

for layer in layers:
	for i in range(SIZE):
		if image[i] == "2":
			image[i] = layer[i]

for row in range(HEIGHT):
	line = ""

	for col in range(WIDTH):
		pixel = image[row * WIDTH + col]
		line += "█" if pixel == "1" else " "

	print (line)
```
- The Javascript version is as follows:
```
const fs = require("fs");

const WIDTH = 25;
const HEIGHT = 6;
const SIZE = WIDTH * HEIGHT;

const data = fs
	.readFileSync("input08", "utf8")
	.trim();

const layers = [];

for (let i = 0; i < data.length; i += SIZE) {
	layers.push(data.slice(i, i + SIZE));
}

const image = Array(SIZE).fill("2");

for (const layer of layers) {
	for (let i = 0; i < SIZE; i++) {
		if (image[i] == "2") {
			image[i] = layer[i];
		}
	}
}

for (let row = 0; row < HEIGHT; row++) {
	let line = "";

	for (let col = 0; col < WIDTH; col++) {
		line += image[row * WIDTH + col] === "1" ? "█" : " ";
	}
	console.log(line);
}
```

# This Concludes Day 08 of The Advent of Code.
