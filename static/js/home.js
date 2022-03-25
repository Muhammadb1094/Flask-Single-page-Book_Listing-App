$(function(){
    var base_url = document.getElementById("base_url").value;

    fetch( base_url + '/get_all_books/')
      .then((response) => {

        return response.json();
      })
      .then((data) => {

        var books = data.books;

        let list = document.getElementById("myList");

        if (books.length ==0){

            let li = document.createElement("li");
            li.innerText = "Found Nothing!";
            list.appendChild(li);
        }


        books.forEach((item)=>{


                      let edit = document.createElement("a");
                      edit.innerText = "Edit";
                      edit.id = "edit";

                      edit.classList.add('m-3');


                      edit.onclick = function(event) {

                                document.getElementById("name").value = item["name"];
                                document.getElementById("name").readOnly = true;
                                document.getElementById("description").value = item["description"];
                                document.getElementById("head").innerHTML  = "Enter Updated Text" ;
                      }



                      let deletes = document.createElement("a");
                      deletes.href = "http://127.0.0.1:5000/delete/" + item["id"] + "/";
                      deletes.id = "delete";
                      deletes.innerText = "Delete";

                      deletes.classList.add('m-3');

                      let span = document.createElement("span");
                      span.innerText = "     |     ";
                      span.classList.add('h4');

                      let span2 = document.createElement("span");
                      span2.innerText = "     |     ";
                      span2.classList.add('h4');


                      let li = document.createElement("li");
                      li.innerText = "BOOK NAME: " + item["name"];
                      li.classList.add('p-3');

                      li.append(span);

                      li.append("DESCRIPTION: " + item["description"]);

                      li.append(span2);

                      li.append(edit);
                      li.append(deletes);

                      list.appendChild(li);
                });

      });

});