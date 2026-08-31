# URL
https://adventofcode.com/2019/day/14#part2

# Description
After collecting ORE for a while, you check your cargo hold: 1 trillion (1000000000000) units of ORE.

With that much ore, given the examples above:
```
    The 13312 ORE-per-FUEL example could produce 82892753 FUEL.
    The 180697 ORE-per-FUEL example could produce 5586022 FUEL.
    The 2210736 ORE-per-FUEL example could produce 460664 FUEL.
```
Given 1 trillion ORE, what is the maximum amount of FUEL you can produce?

# Method of Solve 
- The Part 02 of this challenge can be solved as follows:
- The Python version is as follows:
```
import math


with open("input14", "r") as f:
	reactions_input = f.read().strip().splitlines()


reactions = {}


for line in reactions_input:

	left, right = line.split(" => ")

	inputs = []


	for part in left.split(", "):

		amount, chemical = part.split()

		inputs.append(
			(int(amount), chemical)
		)


	output_amount, output_chemical = right.split()

	reactions[output_chemical] = (
		int(output_amount),
		inputs
	)


def get_ore(fuel_amount):

	leftovers = {}


	def produce(chemical, amount):

		if chemical == "ORE":
			return amount


		available = leftovers.get(
			chemical,
			0
		)


		if available >= amount:

			leftovers[chemical] = available - amount

			return 0


		if available > 0:

			amount -= available

			leftovers[chemical] = 0


		output_amount, ingredients = reactions[chemical]


		batches = math.ceil(
			amount / output_amount
		)


		produced = batches * output_amount


		extra = produced - amount


		leftovers[chemical] = leftovers.get(
			chemical,
			0
		) + extra


		ore = 0


		for ingredient_amount, ingredient in ingredients:

			ore += produce(
				ingredient,
				ingredient_amount * batches
			)


		return ore


	return produce(
		"FUEL",
		fuel_amount
	)


ORE_LIMIT = 1_000_000_000_000


low = 1
high = 1


while get_ore(high) <= ORE_LIMIT:
	high *= 2


while low <= high:

	mid = (low + high) // 2

	ore_required = get_ore(mid)


	if ore_required <= ORE_LIMIT:

		low = mid + 1

	else:

		high = mid - 1


print(f"Maximum FUEL: {high}")
```
- The Javascript version is as follows:
```
const fs = require("fs");

const lines = fs
	.readFileSync("input14", "utf-8")
	.trim()
	.split("\n");


const reactions = new Map();


for (const line of lines) {

	const [left, right] = line.split(" => ");

	const inputs = [];


	for (const part of left.split(", ")) {

		const [amount, chemical] = part.split(" ");

		inputs.push({
			amount: Number(amount),
			chemical: chemical
		});
	}


	const [outputAmount, outputChemical] = right.split(" ");


	reactions.set(
		outputChemical,
		{
			amount: Number(outputAmount),
			inputs: inputs
		}
	);
}


function getOre(fuelAmount) {

	const leftovers = new Map();


	function produce(chemical, amount) {

		if (chemical === "ORE") {
			return amount;
		}


		const available = leftovers.get(
			chemical
		) ?? 0;


		if (available >= amount) {

			leftovers.set(
				chemical,
				available - amount
			);

			return 0;
		}


		if (available > 0) {

			amount -= available;

			leftovers.set(
				chemical,
				0
			);
		}


		const reaction = reactions.get(
			chemical
		);


		const batches = Math.ceil(
			amount / reaction.amount
		);


		const produced = batches * reaction.amount;


		const extra = produced - amount;


		leftovers.set(
			chemical,
			(leftovers.get(chemical) ?? 0) + extra
		);


		let ore = 0;


		for (const ingredient of reaction.inputs) {

			ore += produce(
				ingredient.chemical,
				ingredient.amount * batches
			);
		}


		return ore;
	}


	return produce(
		"FUEL",
		fuelAmount
	);
}


const ORE_LIMIT = 1_000_000_000_000;


let low = 1;
let high = 1;


while (getOre(high) <= ORE_LIMIT) {
	high *= 2;
}


while (low <= high) {

	const mid = Math.floor(
		(low + high) / 2
	);


	const oreRequired = getOre(mid);


	if (oreRequired <= ORE_LIMIT) {

		low = mid + 1;
	}

	else {

		high = mid - 1;
	}
}


console.log(`Maximum FUEL: ${high}`);
```

# This Concludes Day 14 of The Advent of Code.
