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
