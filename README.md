# Mouse Activity Analysis with AI

## Project Overview
This project is part of a senior design initiative to analyze mouse activity and detect fraudulent behaviors such as the use of mouse jigglers. The aim is to leverage artificial intelligence (AI) to distinguish genuine human mouse movements from automated patterns, enhancing workplace monitoring tools.

## Features
- **Mouse Data Collection**: C++ code to record X-Y coordinates of mouse movements.
- **Fraudulent Activity Detection**: AI model trained on real and synthetic data to identify fraudulent behaviors.
- **Integration**: AI-powered fraud detection embedded into a desktop productivity analysis application.
- **Deployment**: Cloud and on-premises licensing options.

## Technologies Used
- **Programming Languages**: C++, Python, R
- **AI Frameworks**: scikit-learn, TensorFlow
- **Data Visualization**: ggplot2 (R)

## Project Structure
- `main.cpp`: C++ code to record mouse movements and save them to timestamped files.
- `project.md`: Detailed project documentation, including workflow, AI modeling plans, and future steps.
- Sample Files:
  - `mouse_coordinates_2024109_205723.txt`
  - `mouse_coordinates_2024112_1412.txt`

## Getting Started
### Prerequisites
- A Windows machine with Visual Studio for running the C++ code.
- Python installed with libraries: `scikit-learn`, `TensorFlow`, `pandas`.
- R installed with packages: `ggplot2`, `caret`.

### Running the Project
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd mouse-activity
   ```
3. Compile and run the C++ code to generate mouse activity files:
   ```bash
   g++ main.cpp -o mouse_activity
   ./mouse_activity
   ```
4. Process the generated files in Python or R for AI training.

## AI Workflow
1. **Data Collection**:
   - Collect real mouse activity data using `main.cpp`.
   - Simulate fraudulent movements for training.
2. **Model Training**:
   - Train AI models using Python or R.
   - Evaluate performance using metrics like accuracy, precision, and recall.
3. **Integration**:
   - Export the trained model and integrate it into the productivity analysis application.

## Future Enhancements
- Extend fraud detection to include keyboard activity.
- Enhance model performance with more robust datasets.
- Explore applications in cybersecurity and human-robot interaction.

## License
This project is licensed under the MIT License. See the LICENSE file for details.



