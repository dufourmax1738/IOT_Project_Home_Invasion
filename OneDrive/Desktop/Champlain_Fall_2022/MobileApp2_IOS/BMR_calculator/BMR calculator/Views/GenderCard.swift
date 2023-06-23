//
//  GenderCard.swift
//  BMR calculator
//
//  Created by Victor Ssuto on 2022-09-13.
//

import SwiftUI

struct GenderCard: View {

    
    @EnvironmentObject var calculator: Calculator
    
    @State private var selectedGender: Gender = .male
    
    
    
    var body: some View {
        
        ZStack{
            
            CardBackground()
            
            VStack{
                
                CardLabel(text: "Gender", caption: "Select your gender")
                
                Picker("Gender", selection: $calculator.gender){
                    
                    Text("Male").tag(Gender.male)
                    Text("Female").tag(Gender.female)
                    Text("Other").tag(Gender.other)
                    

    
                    
                    
                }
                .pickerStyle(.segmented)
                .frame(width: 150)
                
                
                
            }
            
            .frame(width: 300, height: 500)
            
            
            
        }
        
        
        
        
        
        
    }
}

struct GenderCard_Previews: PreviewProvider {
    static var previews: some View {
        GenderCard()
    }
}
