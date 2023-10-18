#include <cstdlib>

class Person{
    public:
        Person(int);
        int get();
        void set(int);
        int fib();  //public method to calculate Fibonacci number
    private:
        int age;
        int fib_helper(int n);  //private method for recursive Fibonacci calculation
};

Person::Person(int n){
    age = n;
}

int Person::get(){
    return age;
}

void Person::set(int n){
    age = n;
}

//Recursive Fibonacci calculation
int Person::fib_helper(int n){
    if (n <= 1)
        return n;
    else
        return fib_helper(n-1) + fib_helper(n-2);
}

//Public method to initiate Fibonacci calculation for the person's age
int Person::fib(){
    return fib_helper(age);  //calculate Fibonacci number for the age
}

extern "C"{
    Person* Person_new(int n) {return new Person(n);}
    int Person_get(Person* person) {return person->get();}
    void Person_set(Person* person, int n) {person->set(n);}
    int Person_fib(Person* person) {return person->fib();}  // C bridge for fib
    void Person_delete(Person* person){
        if (person){
            delete person;
            person = nullptr;
        }
    }
}
