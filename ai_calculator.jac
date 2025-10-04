walker smart_calc {
    can process;

    has text: str;

    can process {
        report("Received: " + text);
        # Extract numbers
        nums = [];
        for word in text.split(" ") {
            try {
                nums.append(float(word));
            } catch {
                continue;
            }
        }
        if (len(nums) >= 2) {
            total = 0;
            for n in nums {
                total += n;
            }
            report("The sum is: " + str(total));
        } else {
            report("Please provide at least two numbers.");
        }
    }
}
