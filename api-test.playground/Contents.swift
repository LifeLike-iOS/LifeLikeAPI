import UIKit
import Foundation

let urlString = "https://lifelike-api.herokuapp.com/books/5bcf685ba9a32a8279da36b1"
 let defaultSession = URLSession(configuration: .default)

if let url = URL(string: urlString) {
    let dataTask = defaultSession.dataTask(with: url) { (data, response, error) in
        if let error = error {
            print(error)
        }
        else if let data = data,
            let response = response as? HTTPURLResponse,
            response.statusCode == 200 {
            do {
                let dict = try JSONSerialization.jsonObject(with: data, options: [])
                print(dict)
            } catch {
                print(error)
            }
            
        }
    }
    
    dataTask.resume()
}




