//
//  BMR_calculatorApp.swift
//  BMR calculator
//
//  Created by Victor Ssuto on 2022-09-09.
//

import SwiftUI

@main
struct BMR_calculatorApp: App {
    
    @StateObject var calculator: Calculator=Calculator()

    
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(calculator)
        }
    }
}
