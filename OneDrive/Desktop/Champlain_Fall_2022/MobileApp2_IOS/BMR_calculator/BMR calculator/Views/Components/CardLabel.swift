//
//  CardLabel.swift
//  BMR calculator
//
//  Created by Victor Ssuto on 2022-09-09.
//

import SwiftUI

struct CardLabel: View {
    
    var text = "" 
    var caption = ""
    var body: some View {

        Text(text)
            .font(.title)
            .fontWeight(.bold)
            .foregroundColor(Color(.systemBlue))
            .padding(.bottom,10)
        
        Text(caption)
            .font (.caption)
            .foregroundColor(Color(.systemGray))
            .padding(.bottom, 30)

    }
}

struct CardLabel_Previews: PreviewProvider {
    static var previews: some View {
        CardLabel()
    }
}
