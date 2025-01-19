# Senior Design Project: Mouse Activity Analysis with AI

## Project Overview

I am a senior computer engineering student preparing a presentation for my Senior Design Project, which I will develop next semester. The project focuses on detecting fraud in employee activity tracking by analyzing mouse movements using AI.

### Objective
The goal is to determine whether an employee is genuinely working at their desk or using fraudulent methods like mouse jigglers to deceive monitoring software.

### Key Steps
1. **Mouse Activity Data Collection**:
   - A program will be developed to record mouse coordinates over time.
   - The data will be stored in timestamped files for further analysis.

2. **AI Model Training**:
   - The AI will be trained with datasets of both genuine mouse activity and fraudulent activity (e.g., mouse jiggler patterns).
   - The model will be designed to distinguish between genuine and fraudulent behaviors.

3. **Integration**:
   - The trained AI model will be embedded into a desktop application used for employee productivity analysis.
   - The software will be licensed as both a cloud and on-premises solution.

4. **Implementation**:
   - Tools like Python and R will be used for data modeling and AI training.
   - The AI model will be integrated into the C++ desktop application.

---

## Code: Mouse Coordinate Collection

Below is the C++ code developed for recording mouse activity:

```cpp
#include <iostream>
#include <fstream>
#include <windows.h>
#include <ctime>
#include <sstream>

// Function to generate a timestamped filename (without seconds)
std::string getTimestampedFilename() {
    // Generate timestamp
    std::time_t now = std::time(nullptr);
    std::tm localTime;
    localtime_s(&localTime, &now); // Using localtime_s instead of localtime

    std::ostringstream filename;
    filename << "mouse_coordinates_"
        << (localTime.tm_year + 1900)
        << (localTime.tm_mon + 1)
        << localTime.tm_mday << "_"
        << localTime.tm_hour
        << localTime.tm_min << ".txt";  // Removed seconds from filename

    return filename.str();
}

int main() {
    POINT cursorPos;
    std::string currentFilename = getTimestampedFilename();
    std::ofstream file(currentFilename, std::ios::out);

    if (!file) {
        std::cerr << "File could not be opened!" << std::endl;
        return 1;
    }

    std::cout << "Recording mouse coordinates. Press ESC to exit." << std::endl;

    while (true) {
        // Check if the minute has changed to create a new file every 60 seconds
        std::string newFilename = getTimestampedFilename();
        if (newFilename != currentFilename) {
            file.close(); // Close the current file
            currentFilename = newFilename;
            file.open(currentFilename, std::ios::out); // Open a new file

            if (!file) {
                std::cerr << "File could not be opened!" << std::endl;
                return 1;
            }
        }

        // Exit loop if ESC key is pressed
        if (GetAsyncKeyState(VK_ESCAPE)) {
            file.close();
            std::cout << "ESC key pressed. Exiting program." << std::endl;
            return 0;
        }

        if (GetCursorPos(&cursorPos)) {
            // Write mouse coordinates to the file every 100 milliseconds
            file << cursorPos.x << "," << cursorPos.y << std::endl;

            // Also print coordinates to the console
            std::cout << cursorPos.x << "," << cursorPos.y << std::endl;
        }

        // Wait for 100 milliseconds
        Sleep(100);
    }

    return 0;
}
```

---

## Machine Learning Algorithms

### Planned Algorithms
The following machine learning techniques are planned for experimentation:
- **K-Nearest Neighbors (KNN)** for simple pattern classification.
- **Support Vector Machines (SVM)** for identifying linear and non-linear patterns.
- **Deep Learning** (using Neural Networks) for more complex and accurate predictions.

### Fraudulent Movement Generation
To simulate fraudulent movements:
- An algorithm will be developed to create pseudo-random but structured mouse movements.
- A kitchen robot or similar mechanism will be used to generate synthetic datasets by mimicking natural movements with slight variations.

---

## Modeling in Python and R

### Python Workflow
1. **Data Preprocessing**:
   - Mouse coordinate data will be loaded from the generated files.
   - The data will be cleaned and labeled for genuine and fraudulent activities.

2. **Model Training**:
   - Libraries like `scikit-learn` and `TensorFlow` will be used for model development.
   - Model performance will be evaluated using metrics like accuracy, precision, and recall.

3. **Integration**:
   - The trained model will be exported as a `.pkl` or `.h5` file for embedding in the C++ application.

### R Workflow
1. **Data Visualization**:
   - `ggplot2` will be used to visualize patterns in mouse movement data.

2. **Model Training**:
   - Machine learning models will be trained using `caret` or `mlr3`.

3. **Performance Metrics**:
   - Model accuracy and other metrics will be evaluated.

---

### Machine Learning Algorithms and Fraudulent Movement Generation

#### Planned Algorithms
- **K-Nearest Neighbors (KNN)** for simple pattern classification.
- **Support Vector Machines (SVM)** for identifying linear and non-linear patterns.
- **Deep Learning** (using Neural Networks) for more complex and accurate predictions.

#### Fraudulent Movement Generation
- An algorithm will be developed to create pseudo-random but structured mouse movements.
- A kitchen robot or similar mechanism will be used to generate synthetic datasets by mimicking natural movements with slight variations.

---

## Future Steps

### Presentation Preparation
- Tools like PowerPoint and Markdown will be used for documentation and slides.
- Live demos of data collection and modeling will be showcased.

### Prototype Development
- Data analysis will be combined with AI model integration in the desktop application.

### Licensing and Deployment
- Licensing mechanisms will be developed for both cloud and on-premises deployment.

---

## Conclusion
This project combines hardware-level data collection, AI-based analysis, and enterprise-level integration to create an innovative solution for detecting fraud in employee monitoring. The insights gained are expected to improve workplace productivity and trust.
