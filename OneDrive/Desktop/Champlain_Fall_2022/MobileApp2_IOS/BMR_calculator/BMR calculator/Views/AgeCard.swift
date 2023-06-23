//
//  Age-Height-Weight card.swift
//  BMR calculator
//
//  Created by Victor Ssuto on 2022-09-09.
//

import SwiftUI

struct AgeCard: View {
    
    @EnvironmentObject var calculator: Calculator
    
    var body: some View {
    
        
        ZStack{
            
            CardBackground()
            
            VStack{
                
                CardLabel(text: "Age", caption: "Please select your age")
              
                SliderValue(value: calculator.age)
                
                Slider(value: $calculator.age, in: 15...80, step:1.0)
                    .frame(width: 150)
                
                
                
                
            }
            
            
            
        }
        .frame(width: 300, height: 500)

        
        
        
        
        
        
        
        
    }
}

struct AgeCard_previews: PreviewProvider {
    static var previews: some View {
        AgeCard()
    }
}
