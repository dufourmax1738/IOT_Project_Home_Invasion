//
//  Calculator.swift
//  BMR calculator
//
//  Created by Victor Ssuto on 2022-09-13.
//

import Foundation

class Calculator: ObservableObject{
    
    @Published var gender: Gender = Gender.female

    @Published var age: Double = 30
    
    @Published var height: Double = 120
    
    @Published var weight: Double = 60
    
}
