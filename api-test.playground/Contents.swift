import UIKit
import Foundation

let defaultSession = URLSession(configuration: .default)

// Gets one book with endpoint /books/[:id]
if let url = URL(string: "https://lifelike-api.herokuapp.com/books/5bcf685ba9a32a8279da36b1") {
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

// Gets books with endpoint /books/search/[:search_param]
if let url = URL(string: "https://lifelike-api.herokuapp.com/books/search/Arduino%20Projects%20Book") {
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

// Gets all books with endpoint /books
if let url = URL(string: "https://lifelike-api.herokuapp.com/books") {
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




