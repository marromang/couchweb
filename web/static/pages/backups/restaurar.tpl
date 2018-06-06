%include('header.tpl')
<div class="content-wrapper">
  <section class="content-header">
    
      <div class="box box-maroon">
        <div class="box-header with-border">
          <h3 class="box-title">Elección de host</h3>
        </div>
        <div class="box-body">
          <form action="/restaurar2" method="post">
            <div class="form-group">
              <label>Host</label>
              <select class="form-control" name="host">
	      	<option>stark</option>
		<option>pepper</option>
		<option>todos</option>
              </select>
            </div>
            <div class="form-group">
              <button class="btn btn-success">Siguiente</button>
            </div>
          </form>
        </div>
      </div>
    
  </section>
</div>
%include('footer.tpl')

