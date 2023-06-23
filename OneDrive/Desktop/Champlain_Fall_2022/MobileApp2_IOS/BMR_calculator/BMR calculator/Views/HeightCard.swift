//
//  HeightCard.swift
//  BMR calculator
//
//  Created by Victor Ssuto on 2022-09-09.
//

import SwiftUI

struct HeightCard: View {
    
    @EnvironmentObject var calculator: Calculator

    var body: some View {

        ZStack{
            
            CardBackground()
            
            
            VStack{
                
                CardLabel(text: "Height", caption: "Please select your height")
              
                SliderValue(value: calculator.height)
                
                Slider(value: $calculator.height, in: 100...200, step:1.0)
                    .frame(width: 150)
                
                
                
            }
            
            
            
        }
        .frame(width: 300, height: 500)

        
        
        
        

    }
}

struct HeightCard_Previews: PreviewProvider {
    static var previews: some View {
        HeightCard()
    }
}
