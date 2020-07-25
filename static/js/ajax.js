$(document).ready(function(){

/*     var contactForm = $(".contact-form")
    var contactFormMethod = contactForm.attr("method")
    var contactFormEndpoint = contactForm.attr("action")

    contactForm.submit(function(event){
        event.preventDefault();
        var contactFormData = contactForm.serialize()
        var thisForm = $(this)

        $.ajax({
            url: contactFormEndpoint,
            method: contactFormMethod,
            data: contactFormData,
            
            success: function(data){
                contactForm[0].reset()
                
            },

            error: function(errorData){
                    alert("خطایی رخ داده است")
            }
    })
}) */
    var ClassForm = $(".class_form")

    ClassForm.submit(function(event){
        event.preventDefault();

        var thisForm = $(this)
        var actionEndpint = thisForm.attr("data-endpoint");
        var httpMethod = thisForm.attr("method");
        var formData = thisForm.serialize();


        $.ajax({
            url: actionEndpint,
            method: httpMethod,
            data: formData,
            
            success: function(data){
                var submitForm = thisForm.find(".submit-span");
                
                if(data.added){
                    submitForm.html("<input type='submit' value='انصراف' class='input' />")
                }

                else if (! data.added){
                    submitForm.html("<input type='submit' value='ثبت نام' class='input' />")
                }

                 var cartCount = $(".cart")
                 cartCount.text(data.cartItemCount)
                 
                 var currentPath = window.location.href
                 if (currentPath.indexOf("profile") != -1){
                     refreshRegisters()
                 }
                
            },

            error: function(errorData){
                    alert("خطایی رخ داده است")
                     location.reload();
            }
        })
    })


    function refreshRegisters(){
        var registersTable = $(".registers-table")
        var registersBody = registersTable.find(".registers-body")
        var classRows = registersBody.find(".registered-class")
        var currentPath = window.location.href
        
        var refreshRegisterUrl = 'api/profile';
        var refreshRegisterMethod = "GET";
        var data = {};

        $.ajax({
            url: refreshRegisterUrl,
            method: refreshRegisterMethod,
            data: data,
            
            success: function(data){
            var hiddenCartItemRemoveForm = $(".cart-item-remove-form")
            
            if  (data.classes.length > 0){
                
                classRows.html(" ")
                i = data.classes.length
                var classes = data.classes.reverse();
                $.each(data.classes, function(index, value){
                    location.reload();
                    var newCartItemRemove = hiddenCartItemRemoveForm.clone()
                    newCartItemRemove.find(".cart-item-class-id").val(value.id)
                    registersBody.prepend("<tr>\
                                            <th scope=\"row\">" + i + "</th>\
                                            <td>" + value.title + "</td>\
                                            <td>" + value.price + "</td>\
                                            <td class=\"buttons\">" + newCartItemRemove.html() + "<a class=\"detail\" href=\"{% url 'class_details' class.id %}\">مشاهده جزئیات</a>" + "</td>\
                                            </tr>")
                    
                    i--  

                })

                   registersBody.find(".subtotal").text(data.subtotal)
                   registersBody.find(".total").text(data.total)

            }
            else{
                window.location.href = currentPath
            }
            
            },
            error: function(errorData){
                alert("خطایی رخ داده است")
            }
        })
    
    
    }


})

