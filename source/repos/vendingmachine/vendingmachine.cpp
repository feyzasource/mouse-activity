#include <iostream>
#include <map>

class VendingMachine {
public:
    VendingMachine() {
        products = {
            {"Water", 3},
            {"Snickers", 4},
            {"Coffee", 5}
        };
        balance = 0;
    }

    void insertMoney(int amount) {
        if (amount == 1 || amount == 5 || amount == 10) {
            balance += amount;
            std::cout << "Inserted: $" << amount << " | Current balance: $" << balance << std::endl;
        }
        else {
            std::cout << "Invalid amount! Only 1, 5, and 10 USD are accepted.\n";
        }
    }

    void selectProduct(const std::string& product) {
        if (products.find(product) != products.end()) {
            int cost = products[product];
            if (balance >= cost) {
                balance -= cost;
                std::cout << "Dispensing " << product << ". Remaining balance: $" << balance << std::endl;
            }
            else {
                std::cout << "Insufficient balance for " << product << ". Please insert $" << (cost - balance) << " more.\n";
            }
        }
        else {
            std::cout << "Invalid selection!\n";
        }
    }

    void showMenu() {
        std::cout << "\n--- Product Menu ---\n";
        for (const auto& item : products) {
            std::cout << item.first << ": $" << item.second << "\n";
        }
    }

private:
    std::map<std::string, int> products;
    int balance;
};

int main() {
    VendingMachine machine;
    int choice, amount;
    std::string product;

    std::cout << "Welcome to the Vending Machine!\n";
    machine.showMenu();

    while (true) {
        std::cout << "\nOptions:\n1. Insert Money\n2. Select Product\n3. Exit\nChoose an option: ";
        std::cin >> choice;

        switch (choice) {
        case 1:
            std::cout << "Enter amount (1, 5, or 10 USD): ";
            std::cin >> amount;
            machine.insertMoney(amount);
            break;
        case 2:
            std::cout << "Enter product name (Water, Snickers, Coffee): ";
            std::cin >> product;
            machine.selectProduct(product);
            break;
        case 3:
            std::cout << "Thank you for using the vending machine. Goodbye!\n";
            return 0;
        default:
            std::cout << "Invalid choice. Try again.\n";
        }
    }
}
