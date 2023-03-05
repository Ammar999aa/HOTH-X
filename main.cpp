#include <iostream>
#include<string>
#include<cmath>
#include<vector>
#include<algorithm>
#include<ctime>
#include<sstream>
using namespace std;

int main() {
    string start, end, car, plane;
      time_t tdate,rdate;
	vector<string> trans;
    
	cout << "Welcome to Boujie Budget!"<<endl;
	cout << "Please enter your pick up location: ";
	getline(cin,start, '\n');
	cout << "Please enter your drop off location: ";
	getline(cin, end, '\n');
    cout << "Please enter the date of travel (YYYY-MM-DD): ";
    cin >> tdate;
    struct tm tm{};
   // tdate== mktime(strptime(tdate, "%Y-%m-%d", &tm));
  
   
    cout << "Please enter the date of return (YYYY-MM-DD): ";
    cin >> rdate; 
    double duration = difftime(tdate, rdate); duration /= (60 * 60 * 24);
    cout << "Duration of stay: " << duration << " days." << endl;
    std::string ans;
    std::cin >> ans;
    cout << "Please select  your deired means of transportation: "<< endl;
    std::vector<std::string> userInputs; // declare a vector to store user input
    cout << "A) car  B) bus  C) plane "<<endl;
    

    
    trans.push_back(ans); // store user input in vector

    if (ans == "A") {
        std::cout << "What is your preferred car type? ";
        std::string carType;
        std::cin >> carType;
        userInputs.push_back(carType); // store user input in vector

        std::cout << "What year would you like your car to be? ";
        int carYear;
        std::cin >> carYear;
        userInputs.push_back(std::to_string(carYear)); // store user input in vector

        std::cout << "Your preferred means of transportation is a " << carYear << " " << carType << "." << std::endl;
    }

   
    // print out all user inputs stored in the vector
    
	//if statement and for loops

	cout << " Your estimated budget is: ";
	return 0;
}