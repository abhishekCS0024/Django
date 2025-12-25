#include <iostream>
#include <thread>
#include <mutex>

std::mutex r1, r2;

void process1() {
    r1.lock();
    std::this_thread::sleep_for(std::chrono::milliseconds(100)); // Simulate delay
    r2.lock();  // Waiting for r2, which is locked by process2
    std::cout << "Process 1 executed\n";
    r2.unlock();
    r1.unlock();
}

void process2() {
    r2.lock();
    std::this_thread::sleep_for(std::chrono::milliseconds(100));
    r1.lock();  // Waiting for r1, which is locked by process1
    std::cout << "Process 2 executed\n";
    r1.unlock();
    r2.unlock();
}

int main() {
    std::thread t1(process1);
    std::thread t2(process2);
    
    t1.join();
    t2.join();

    return 0;
}
