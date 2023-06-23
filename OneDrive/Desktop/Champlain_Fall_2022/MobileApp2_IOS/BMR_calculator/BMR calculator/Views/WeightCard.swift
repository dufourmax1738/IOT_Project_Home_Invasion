//
//  WeightCard.swift
//  BMR calculator
//
//  Created by Victor Ssuto on 2022-09-09.
//

import SwiftUI

struct WeightCard: View {
    
    @EnvironmentObject var calculator: Calculator

    var body: some View {

        ZStack{
            
            CardBackground()
            
            
            VStack{
                
                CardLabel(text: "Weight", caption: "Please select your weight")
              
                SliderValue(value: calculator.weight)
                
                Slider(value: $calculator.weight, in: 50...200, step:1.0)
                    .frame(width: 150)
            }
            
            
            
        }
        .frame(width: 300, height: 500)

        
        
        


    }
}

struct WeightCard_Previews: PreviewProvider {
    static var previews: some View {
        WeightCard()
    }
}
