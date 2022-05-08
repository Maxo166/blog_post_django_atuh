$( function () {
    $( ".navbar-burger" ).click( function () {
        $( "#navbarBasicExample" ).slideToggle( 'fast' );
    } )
    $( '.navbar-item.has-dropdown a.navbar-link' ).on( 'click', function () {
        $( '.navbar-dropdown' ).slideToggle( 'fast' )
    } );
    $( '.comment-dropdown-trigger button' ).on( 'click', function () {
        $( this ).parent()
            .next( '.comment-dropdown-menu' )
            .slideToggle( 'fast' )
    } );
    $( 'input#id_title' ).focusin( function () {
        $( this ).css( { 'width': '100%' } );
    } );
    $( 'input#id_title' ).focusout( function () {
        $( this ).css( { 'width': '30rem' } );
    } );
    
} );