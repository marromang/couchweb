%include('header.tpl')
<div class="content-wrapper">
<section class="content">
    <div class="row">
        <div class="col-xs-12">
            <div class="box">
                <div class="box-header">
                    <h3 class="box-title">Hosts</h3>
                </div>
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
                            <td>172.22.200.101</td>
                            %if stark:
                                <td><span class="label label-success">Activo</span></td>
                            %else:
                                <td><span class="label label-danger">Inactivo</span></td>
			    % end
                            <td>Servidor principal del entorno.</td>
                        </tr>
                        <tr>
                            <td><a href="/pepper">pepper</a></td>
                            <td>172.22.200.103</td>
                            %if pepper:
                                <td><span class="label label-success">Activo</span></td>
                            %else:
                                <td><span class="label label-danger">Inactivo</span></td>
		            % end
                            <td>Servidor secundario del entorno.</td>
		        </tr>
                        <tr>
                            <td><a href="/jarvis">jarvis</a></td>
                            <td>172.22.200.105</td>
                            %if jarvis:
                                <td><span class="label label-success">Activo</span></td>
                            %else:
                                <td><span class="label label-danger">Inactivo</span></td>
                            % end
			    <td>Monitorización, web, dns</td>
                        </tr>
                    </table>
                </div>
            </div>
        </div>
    </div>
</section>
</div>
%include('footer.tpl')

