// Parent class
class Vehicle {
    String brand;

    Vehicle(String brand) {
        this.brand = brand;
    }

    void displayInfo() {
        System.out.println("Brand: " + brand);
    }
}

// Child class inheriting from Vehicle
class Car extends Vehicle {
    int year;

    Car(String brand, int year) {
        super(brand); // Calling superclass constructor using super keyword
        this.year = year;
    }

    @Override
    void displayInfo() {
        super.displayInfo(); // Calling superclass method using super keyword
        System.out.println("Year: " + year);
    }
}

public class SuperKeywordExample {
    public static void main(String[] args) {
        Car myCar = new Car("Toyota", 2022);
        myCar.displayInfo();
    }
}
