<?php
// Define variables
$name = "John";
$age = 30;
$isStudent = true;

// Output variables
echo "Name: " . $name . "<br>";
echo "Age: " . $age . "<br>";
echo "Is student? " . ($isStudent ? "Yes" : "No") . "<br>";

// Basic arithmetic
$number1 = 10;
$number2 = 5;
$sum = $number1 + $number2;
$difference = $number1 - $number2;
$product = $number1 * $number2;
$quotient = $number1 / $number2;

// Output results
echo "Sum: " . $sum . "<br>";
echo "Difference: " . $difference . "<br>";
echo "Product: " . $product . "<br>";
echo "Quotient: " . $quotient . "<br>";

// Conditional statements
$grade = 85;

if ($grade >= 90) {
    echo "Grade: A";
} elseif ($grade >= 80) {
    echo "Grade: B";
} elseif ($grade >= 70) {
    echo "Grade: C";
} elseif ($grade >= 60) {
    echo "Grade: D";
} else {
    echo "Grade: F";
}

// Looping
echo "<h3>Counting from 1 to 10:</h3>";
for ($i = 1; $i <= 10; $i++) {
    echo $i . "<br>";
}

?>
