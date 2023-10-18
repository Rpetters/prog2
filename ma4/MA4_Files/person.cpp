#include <cstdlib>
class Person{
    public:
        Person(unsigned int);
        unsigned int get();
        void set(unsigned int);
        unsigned int fib();  //public method to calculate Fibonacci number
    private:
        unsigned int age;
        unsigned int fib_helper(unsigned int n);  //private method for recursive Fibonacci calculation
};

Person::Person(unsigned int n){
    age = n;
}

unsigned int Person::get(){
    return age;
}

void Person::set(unsigned int n){
    age = n;
}

//Recursive Fibonacci calculation
unsigned int Person::fib_helper(unsigned int n){
    if (n <= 1)
        return n;
    else
        return fib_helper(n-1) + fib_helper(n-2);
}

//Public method to initiate Fibonacci calculation for the person's age
unsigned int Person::fib(){
    return fib_helper(age);  //calculate Fibonacci number for the age
}

extern "C"{
    Person* Person_new(unsigned int n) {return new Person(n);}
    unsigned int Person_get(Person* person) {return person->get();}
    void Person_set(Person* person, unsigned int n) {person->set(n);}
    unsigned int Person_fib(Person* person) {return person->fib();}  //C bridge for fib
    void Person_delete(Person* person){
        if (person){
            delete person;
            person = nullptr;
        }
    }
}
