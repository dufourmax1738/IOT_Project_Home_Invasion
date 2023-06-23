//
//  NextButton.swift
//  BMR calculator
//
//  Created by Victor Ssuto on 2022-09-13.
//

import SwiftUI

struct NextButton: View {
    var body: some View {
            
        Image (systemName: "chevron.right.circle.fill")
            .font (.largeTitle)
            .foregroundColor(Color(.systemBlue))
            .frame(height: 100)
            .padding(.top,50 )
    }
}

struct NextButton_Previews: PreviewProvider {
    static var previews: some View {
        NextButton()
    }
}
