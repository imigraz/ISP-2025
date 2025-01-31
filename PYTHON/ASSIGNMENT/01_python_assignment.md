Python Assignment

    **File I/O**
       1. Read the file "assignment_text.txt" and extract only numerical values (integers and floating-point numbers, if applicable) from each line.
        Store these numerical values in a list

   ** Loops, Conditions, and Functions**
       2. Write a Python function that takes the list from Assignment 1 as input and finds the smallest even number in the list.
        The function should return:
            The value of the smallest even number
            The position (index) of this number in the list
        Constraints:
            Do not use NumPy or any built-in Python shortcuts (e.g., min() or list comprehensions)
            Implement the solution explicitly using loops and conditional tests

    **NumPy Implementation**
        3. Redo Assignment 2 using NumPy:
            Convert the list from Assignment (1.) into a NumPy array
            Find the smallest even number using Boolean indexing

    **Pandas & Matplotlib**

        4. Using pandas, read in the file "patient_data.csv" and process it as follows:

        Step 1: Load the data

        Step 2: Clean the data
            Strip any extra whitespace from column names and data.
            Drop rows with missing or invalid values in relevant columns (use the pandas dropna() method; check the pandas documentation for the correct syntax).
            Standardize gender values:
                Remove extra symbols like "/" or "."
                Convert all letters to lowercase
            Fill in any missing numerical values with the minimum value in each respective column
            Save the modified DataFrame to a new ".csv" file

        Step 3: Extract and filter BMI data
            From the cleaned DataFrame, extract BMI values separately for:
                Males aged 45+
                Females aged 45+
            Store these filtered datasets separately

        Step 4: Validate the extracted datasets
            Check how many entries exist for male and female BMI data

        Step 5: Visualize BMI distributions
            Plot a histogram for BMI values:
                Females: Color = purple, Transparency (alpha) = 0.5
                Males: Color = red, Equivalent transparency
            Ensure the histograms overlap for comparison

        Step 6: Add plot details
            Set a title for the plot.
            Label the x-axis and y-axis appropriately

        Step 7: Save and submit
            Save the final plot as a .pdf file
            
Submit the assignment ".py" or ".ipynb" file along with the plot in a .zip directory entitled {YOUR_LAST_NAME}_PYTHON_COURSE.zip to iva.pritisanac@medunigraz.at
