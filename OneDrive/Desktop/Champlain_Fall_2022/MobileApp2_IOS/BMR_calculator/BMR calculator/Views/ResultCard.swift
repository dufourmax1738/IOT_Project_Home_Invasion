//
//  ResultCard.swift
//  BMR calculator
//
//  Created by Victor Ssuto on 2022-09-13.
//

import SwiftUI

struct ResultCard: View {
    var body: some View {
        ZStack{
            
            CardBackground()
            
            
            VStack{
                
                CardLabel(text: "Result", caption: "total BMR: ")
              
            }
            
            
            
        }
        .frame(width: 300, height: 500)

        
        
        


    }
}


struct ResultCard_Previews: PreviewProvider {
    static var previews: some View {
        ResultCard()
    }
}
