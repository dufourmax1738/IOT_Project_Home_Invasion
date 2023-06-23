//
//  CardBackground.swift
//  BMR calculator
//
//  Created by Victor Ssuto on 2022-09-09.
//

import SwiftUI

struct CardBackground: View {
    
    
    
    var body: some View {
       
        Color(.white)
            .cornerRadius(20)
            .shadow(color: Color(.systemGray5), radius: 5, x:2, y:2)
        
    }
}

struct CardBackground_Previews: PreviewProvider {
    static var previews: some View {
        CardBackground()
    }
}
