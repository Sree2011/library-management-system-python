// Import the dependencies

import java.util.*;

public class Main{
    public static void main(String[] args) {
        // Display welcome information to the user
        try (Scanner sc = new Scanner(System.in)) {
            // Display welcome information to the user
            System.out.print("Hi! Welcome to our Library Management System!");
            
            String name_user = sc.nextLine();
            System.out.println("Hello, "+name_user);
            System.out.println("If you want to add a book, press 1");
            System.out.println("If you want to see all books, press 2");
            System.out.println("If you want to get a book issued, press 3");
            System.out.println("If you want to return a book, press 4");
            
            int option_book = sc.nextInt();
            
            // Check for the functions
            switch(option_book){
                case 1: add_book();
                case 2: list_books();
                case 3: issue_book();
                case 4: return_book();
                default: System.out.println("Invalid input");
            }
        }
    }

    public static void add_book(){
        
    }

    public static void list_books() {
        throw new UnsupportedOperationException("Not supported yet.");
    }

    public static void issue_book() {
        throw new UnsupportedOperationException("Not supported yet.");
    }

    public static void return_book() {
        throw new UnsupportedOperationException("Not supported yet.");
    }
}