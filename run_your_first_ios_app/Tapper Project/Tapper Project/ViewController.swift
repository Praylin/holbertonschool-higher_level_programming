//
//  ViewController.swift
//  Tapper Project
//
//  Created by praylin on 5/27/16.
//  Copyright © 2016 Praylin. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    
    var taps_done: Int = 0
    var taps_requested: Int? = 0
    
    @IBOutlet weak var image_tapper: UIImageView!
    @IBOutlet weak var button_play: UIButton!
    @IBOutlet weak var textfield_number: UITextField!
    @IBOutlet weak var label_taps: UILabel!
    @IBOutlet weak var button_coin: UIButton!
    
    
//    @IBAction func clickCoinButton(sender: AnyObject) {
//        
//        
//    }
//    @IBAction func clickPlayButton(sender: AnyObject) {
//      textfield_number.text = "Let's do xx taps"
//       
//    }
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

