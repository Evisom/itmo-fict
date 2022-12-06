function request(r, callback) {
    if (r.body) {
        r.body = JSON.stringify(r.body)
    }
    fetch(r.url, {
        headers: {
            'Content-Type': 'application/json'
        },
        method: r.method, 
        body: r.body
    }).then(function(res){ 
        return res.json(); 
    }).then(function(data){ 
        callback(data); 
    })
}


const sort = (arr) => {
    for (let i = 1; i < arr.length; i++) {
      for (let j = 0; j < arr.length - i; j++) {
        if (arr[j][2] > arr[j + 1][2]) {
          [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        }
      }
    }
    return arr;
  };

window.onload = () =>{
    const container = document.getElementById("container");
    const createButton = document.getElementById('create');
    const select = document.getElementById('selectbox');
    const resetButton = document.getElementById('reset');

    const sortButton = document.getElementById('sort');
    const sortRevButton = document.getElementById('sortReverse');
    const dateSelectButton = document.getElementById('dateSelect');

    function transaction(response) {
        const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
        d = new Date(response[3]).toDateString().split(' ')
        element = '<div class="transaction">\
                    <div class="tr-name">'+response[1]+'</div>\
                    <div class="tr-cost">'+response[2]+'$</div>\
                    <div class="tr-date">' + d[2]+' '+d[1]+' '+d[3] + '</div>\
                    <div class="cat">'+response[4]+'</div>\
                    <button class="deleteButton" id = "b'+response[0]+'">x</button>\
                  </div>'
        return element
    }

    function render(url, sortReverse=undefined) { 
        container.innerHTML = ''
        select.innerHTML='<option>Category</option>'

        if (url.includes('getByCategory')) {
            select.innerHTML='<option>'+url.split('?')[1]+'</option>'
        }
        
        request({
            url: url,
            method: 'GET',
            body: undefined
        }, (response)=> {
            console.log(response);
            if (sortReverse == false) {
                response = sort(response)
            } else if (sortReverse == true) {
                response = sort(response)
                response = response.reverse()
            }
            for (let i = 0; i < response.length; i++) {
                container.innerHTML+=transaction(response[i])
            }
            const buttons = document.getElementsByClassName('deleteButton');
            for (let i = 0; i < buttons.length; i++) {
                buttons[i].onclick = function (el) {
                    tr_id = el.target.id.slice(1)
                    request({
                        url: '/deleteTransaction',
                        method: 'POST',
                        body: {
                            id: tr_id 
                        }}, (res)=>{
                            render(url)
                        })
                }
            }
        });   
        request({
            url: '/getCategories',
            method: 'GET',
            body: undefined
        }, (response) => {
            console.log(response)
            for (let i = 0; i < response.length; i++) {
                select.innerHTML+='<option id="b'+i+'">'+response[i]+'</option>'
            }
            select.onchange = () => {
                console.log(response[select.selectedIndex-1])
                render('/getByCategory?category='+response[select.selectedIndex-1][0])
                
            }
        }) 
        sortButton.onclick = function() {
            render(url, false)
        }
        sortRevButton.onclick = function() {
            render(url, true)
        }

        dateSelectButton.onclick = function() {
            const sdate = document.getElementById('sdate').value;
            const edate = document.getElementById('edate').value;
            url = '/getByDate?startDate='+new Date(sdate).getTime()+'&endDate=' + new Date(edate).getTime()
            render(url)
        }

    }
    resetButton.onclick = ()=>{render('/getAllTransactions')}

    render('/getAllTransactions')
    createButton.onclick = function() {
        const data = {name: document.getElementById('name').value,
                      cost: document.getElementById('cost').value,
                      date: new Date(document.getElementById('date').value).getTime(),
                      categories: document.getElementById('categories').value}
        console.log(data)
        if (isNaN(data.cost)) {
            alert('Cost must be a number')
            return 
        }
        request({
            url: '/createTransaction',
            method: 'POST',
            body: data
        }, (response)=> {
            console.log(response);
            render('/getAllTransactions')
        });

    }



 

}