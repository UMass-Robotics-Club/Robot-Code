FROM arm64v8/ros:humble

RUN sed --in-place --expression \
      '$ibash && source "/opt/ros/humble/setup.bash" && source "/opt/ros/humble/local_setup.bash"' \
      /ros_entrypoint.sh
RUN echo 'source /opt/ros/humble/setup.bash' >> /root/.bashrc
RUN echo 'source /opt/ros/humble/local_setup.bash' >> /root/.bashrc


#RUN /bin/bash -c 'source "/opt/ros/humble/setup.bash" && source "/opt/ros/humble/local_setup.bash"'
#RUN /bin/bash -c 'export PATH=$PATH:/opt/ros/humble/bin'
#COPY ./ros_entrypoint.sh /ros_entrypoint.sh
#RUN /bin/bash -c 'chmod +x /ros_entrypoint.sh'
