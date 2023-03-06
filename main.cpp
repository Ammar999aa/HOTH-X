#include <iostream>
#include<string>
#include<cmath>
#include<vector>
#include<algorithm>
#include<ctime>
#include<cstring>
#include<sstream>

using namespace std;

int main() {
    string start, end, car, plane, timestr,timestr2;
      string tdate,rdate;
	vector<string> trans;
    
	cout << "Welcome to Boujie Budget!"<<endl;
	cout << "Please enter your pick up location: ";
	getline(cin,start, '\n');
	cout << "Please enter your drop off location: ";
	getline(cin, end, '\n');
   cout << "Please enter the date of travel (YYYYMMDD): ";
  cin >> tdate;
  //  //getline(cin, timestr);
  //  
  // struct tm tm{};
  // memset(&tm, 0, sizeof(struct tm));
  // // strptime(timestr.c_str(), "%Y-%m-%d", &tm);
  // // std::tm tm = {};
  ////  time_t date_time = std::mktime(&tm);
  //  
  ////  cout << "Date as time_t: " << date_time << std::endl;
   cout << "Please enter the date of return (YYYY-MM-DD): ";
  cin >> rdate; 
  // double duration = difftime(rdate, tdate);
  // 
  //duration /= (60 * 60 * 24);
  //  cout << "Duration of stay: " << duration << " days." << endl;
   
    std::tm tm1 = {}, tm2 = {};
    tm1.tm_year = std::stoi(tdate.substr(0, 4)) - 1900;
    tm1.tm_mon = std::stoi(tdate.substr(4, 2)) - 1;
    tm1.tm_mday = std::stoi(tdate.substr(6, 2));
    tm2.tm_year = std::stoi(rdate.substr(0, 4)) - 1900;
    tm2.tm_mon = std::stoi(rdate.substr(4, 2)) - 1;
    tm2.tm_mday = std::stoi(rdate.substr(6, 2));
    std::time_t t1 = std::mktime(&tm1);
    std::time_t t2 = std::mktime(&tm2);

    double duration = difftime(t2, t1);
    duration /= (60 * 60 * 24);
    std::cout << "Duration of stay: " << duration << " days." << std::endl;
    cout << "Please select  your deired means of transportation: "<< endl;
    std::vector<std::string> userInputs; // declare a vector to store user input
    cout << "A) car  B) bus  C) plane "<<endl;
     std::string ans;
    std::cin >> ans;

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
    else if (ans == "B") {
        
    }
    else if (ans == "C") {

    }
    else {
        cout << "Input is invalid. Please try again.";
        cout << "Please select  your deired means of transportation: " << endl;
        std::vector<std::string> userInputs; // declare a vector to store user input
        cout << "A) car  B) bus  C) plane " << endl;
        std::cin >> ans;
    }

   
    // print out all user inputs stored in the vector
    
	//if statement and for loops

	cout << " Your estimated budget is: ";
	return 0;
}