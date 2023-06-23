//
//  TitleCard.swift
//  BMR calculator
//
//  Created by Victor Ssuto on 2022-09-09.
//

import SwiftUI

struct TitleCard: View {
    var body: some View {
        
        ZStack{
            
            CardBackground()
            
            
            VStack{
                
                CardLabel(text: "BMR calculator", caption: "for a healthier lifestyle")
              
            }
            
            
            
        }
        .frame(width: 300, height: 500)

    }
}

struct TitleCard_Previews: PreviewProvider {
    static var previews: some View {
        TitleCard()
    }
}
