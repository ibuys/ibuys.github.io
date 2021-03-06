--- 
layout: post
title: Managing Nagios Configs
tags: [sysadmin, nagios]
---

We don't have a very big Nagios installation, comparatively anyway, but it is big enough to find that the default layout for configurations is insane.  I tried using the provided layout, until I wound up with single text files with thousands of lines in them. This made it very hard to do individual customizations for servers, and separating out who wants to be notified for what.  Here is what I came up with for managing our Nagios configs.  

It seems that the repositories are always behind in Nagios, so it is one of the very few apps that I recommend installing from source.  I install Nagios in /usr/local/nagios, the default when compiling, I'll just call it $nag.  The Nagios binary is in $nag/bin, the plugins in $nag/libexec, and the config files in $nag/etc. The easiest way to understand nagios is to follow its start up procedures.  I keep an /etc/init.d/nagios file for initialization, The file defines, among other things, where the home directory for Nagios is, what config file to use as its base, and where the Nagios binary and plugins are.  The important thing to understand is that this file is the first pointer in a long string of pointers that Nagios uses for configuration.  

Inside the nagios.cfg file are the cfg_dir directives.  These are pointers that tell Nagios that it can find additional configurations inside the directories listed.   Once Nagios is given a directory to look at, it will read each file ending in .cfg inside of that directory.  The first directory that I have listed is $nag/etc/defaults.  I keep four files in this directory: commands.cfg, dependencies.cfg, generic.cfg, and timeperiods.cfg.  

The file "commands.cfg" contains the definitions of all check commands that Nagios can understand.  They look like this:


	 # 'check_local_load' command definition
	 define command{
	        command_name    check_local_load
	        command_line    $USER1$/check_load -w $ARG1$ -c $ARG2$
	        }

The file also contains the alert commands, or what Nagios will do when it finds something that it needs to let you know about:


	define command{
	command_name notify-by-email
	command_line	/usr/bin/printf "%b" "***** Nagios *****\n\nNotification Type: 	$NOTIFICATIONTYPE$\nHost: $HOSTNAME$\nState: $HOSTSTATE$\nAddress: 	$HOSTADDRESS$\nInfo: $HOSTOUTPUT$\n\nDate/Time: $LONGDATETIME$\n" | /usr/	bin/mail -s "** $NOTIFICATIONTYPE$ Host Alert: $HOSTNAME$ is $HOSTSTATE$ **" 	$CONTACTEMAIL$
	}

This allows us to call a command later in Nagios by it's defined command_name,such as check_local_load, instead of having to call the entire command including arguments.  Keeps the configs clean.

The next file, "generic.cfg", contains templates for host configurations.  This file allows us to do two things: list common options that are defined for all of the hosts, and separate hosts into notification groups.  The definitions look like this:

	define host{
	        name                            generic-admin
	        notifications_enabled           1
	        event_handler_enabled           1
	        flap_detection_enabled          1
	        process_perf_data               1
	        retain_status_information       1
	        retain_nonstatus_information    1
	        register                        0
	        check_command           check-host-alive
	        max_check_attempts      3
	        notification_interval   120
	        notification_period     24x7
	        notification_options    d,u,r
					contact_groups          admin,admin_pager
	        action_url /nagios/pnp/index.php?host=$HOSTNAME$
	        }

There are two separate types of generic definitions, hosts and services, for the two types of monitoring that Nagios does.  The important section for most of my purposes above is the "contact_groups" line.  This allows me to group contacts with hosts, so it answers the question of "who gets notified if this server goes down?".  The same thing applies to the service template below.

	define service{
	        name                            generic-full	
	        active_checks_enabled           1
	        passive_checks_enabled          1
	        parallelize_check               1
	        obsess_over_service             1
	        check_freshness                 0
	        notifications_enabled           1
	        event_handler_enabled           1
	        flap_detection_enabled          1
	        process_perf_data               1
	        retain_status_information       1
	        retain_nonstatus_information    1
	        register                        0
	        is_volatile                     0
	        check_period                    24x7
	        max_check_attempts              3
	        normal_check_interval           5
	        retry_check_interval            1
	        notification_interval           120
	        notification_period             24x7
	        notification_options            w,c,r
		contact_groups                  admins,admin_pager,webmin
		process_perf_data 1
		action_url /nagios/pnp/index.php?host=$HOSTNAME$&srv=$SERVICEDESC$
	        }

The other two files, timeperiods.cfg and dependencies.cfg, I haven't done a whole lot with yet.

The next directory parsed as defined in nagios.cfg is $nag/etc/users, which, surprisingly enough, is where all of the users are defined.  I keep two files in this directory, users.cfg and contactgroups,cfg.  The users.cfg file contains a list of every user, and since I have different needs for pagers and regular email alerts, each user is defined twice:

	define contact{
	        contact_name                    Jon
	        alias                           Jon Buys
	        service_notification_period     24x7
	        host_notification_period        24x7
	        service_notification_options    w,u,c,r
	        host_notification_options       d,u,r
	        service_notification_commands   service-notify-by-email
	        host_notification_commands      host-notify-by-email
	        email                           jbuys@dollarwork.com
	        }
	
	define contact{
	        contact_name                    Jon_pager
	        alias                           Jon Buys
      	  service_notification_period     24x7
      	  host_notification_period        24x7
      	  service_notification_options    u,c,r
      	  host_notification_options       d,u,r
      	  service_notification_commands   notify-for-disk
      	  host_notification_commands      host-notify-by-email
      	  email 				5555555555@my.phone.company.net
      	  }

This lets me group the users more effectively in the second file, contactgroups.cfg:

	define contactgroup{
	        contactgroup_name admins
      	  alias           sysadmins
      	  members Jon,Gary,nagios_alerts
      	  }
	
	define contactgroup{
	        contactgroup_name admin_pager
	        alias           sysadmin pagers
	        members Jon_pager,Gary_pager,OSS_Primary_Phone,nagios_alerts
	}

Now, check the definitions in the generic.cfg file above, and you'll start to see the chain of config files coming together. The glue sticking it all together is the server definition files.  Each logical group of servers gets their own directory, defined in nagios.cfg.  For example, we have a  group of servers that provides a specific web service  (which I'll call "mesh"), there are web servers, application servers, and database servers that I group together in one directory, named "mesh".  Inside of this directory, each server has its own config file, named like $hostname.cfg.  There is also a mesh.cfg, which groups all of the servers together in a host group.  The $hostname.cfg files look like this:

	 define host{
	        use                     generic-host
      	  host_name              	m-app1 
      	  alias                   m-app1
      	  address                 10.10.10.1
      	  }
	
	define service{
      	  use                             generic-full
      	  host_name                       m-app1
      	  service_description             PING
      	  check_command                   check_ping!100.0,20%!500.0,60%
      	  }
	
	define service{
      	  use                             generic-full
      	  host_name                       m-app1
      	  service_description             DISKUSE
      	  check_command                   check_nrpe!check_df
      	  }

Each server has a host definition at the top, and all of the services that are monitored on that server at the bottom.  The first section's line "use	generic-host" calls the "generic-host" template from the generic.cfg file above.  Each subsequent "define service" section has a "use" line that also calls the templates defined in generic.cfg.  Putting each server in its own file makes it very easy to add and remove servers from Nagios.  To remove them, just remove (or, safer, rename) the $hostname.cfg file and delete the name from the $groupname.cfg file.  It's also very easy to script the creation of new hosts given a list of host names and IP addresses.  

The mesh.cfg file contains the hostgroup configuration for the group:

	define hostgroup{
       	 hostgroup_name  mesh
       	 alias           Mesh Production
       	 members         mdbs1,mdbs2,mdbs3,mdbs4,mdbs5,mdbs6,mdbs7,m-app1,m-app2,m-app3,m-store1,m-store2,m-nfs1,m-nfs2
       	 }

This file is not as important, but it makes the Nagios web interface a little more helpful.  

You'll also notice that the check_command line above contains "check_nrpe!check_df".  This means that I use the nrpe (Nagios Remote Plugin Execution) add-on to actually monitor the services on the remote hosts.  Each server has nrpe installed, and has one configuration file (/usr/local/nagios/etc/nrpe.cfg).  The nrpe.cfg file has a corresponding line that says 

	command[check_df]=/usr/local/nagios/libexec/check_disk -e -L -w 6% -c 4%

This translates the check_df command sent by the check_nrpe command into the longer command defined above.  This makes it easy to install and configure nrpe once, then zip up the  /usr/local/nagios directory and unzip it on all new servers.  

Nagios is nearly limitless in its abilities, but but because of the complexity of its configuration it can be daunting to newcomers.  This setup is designed to make it just a little bit easier to understand, and easier to script.  
