%include('header.tpl')

<div class="content-wrapper">
<section class="content">

	<div class="row">
        	<div class="col-xs-12">
          		<div class="box">
            			<div class="box-header">
             				 <h3 class="box-title">Hosts</h3>
              			<div class="box-tools">
                			<div class="input-group input-group-sm" style="width: 150px;">
                  				<input type="text" name="table_search" class="form-control pull-right" placeholder="Search">
					<div class="input-group-btn">
                    				<button type="submit" class="btn btn-default"><i class="fa fa-search"></i></button>
                  			</div>
                			</div>
              			</div>
            			</div>
            <!-- /.box-header -->
            	<div class="box-body table-responsive no-padding">
              		<table class="table table-hover">
                		<tr>
                  			<th>Nombre</th>
                  			<th>IP</th>
                  			<th>Status</th>
                  			<th>Descripcion</th>
                		</tr>
                		<tr>
                  			<td><a href="/stark">stark</a></td>
                 	 		<td>172.22.100.101</td>
                  			<td><span class="label label-success">Activo</span></td>
                  			<td>Servidor principal del entorno.</td>
                		</tr>
                		<tr>
                  			<td><a href="/pepper">pepper</a></td>
                  			<td>172.22.100.103</td>
                  			<td><span class="label label-success">Activo</span></td>
                  			<td>Servidor secundario del entorno.</td>
                		</tr>
                		<tr>
                  			<td><a href="/jarvis">jarvis</a></td>
                  			<td>172.22.100.105</td>
                  			<td><span class="label label-success">Activo</span></td>
                  			<td>Monitorización, web, dns</td>
                		</tr>
              		</table>
            	</div>
            <!-- /.box-body -->
          </div>
          <!-- /.box -->
	</div>
</section>
</div>
</div>
%include('footer.tpl')
