#include <opencv2/opencv.hpp>
#include <iostream>
#include <vector>
#include <arpa/inet.h>
#include <unistd.h>

#define UDP_PORT 5005
#define BUFFER_SIZE 65507  // Max UDP Packet Size

int main() {
    int sockfd;
    struct sockaddr_in servaddr, cliaddr;
    char buffer[BUFFER_SIZE];
    socklen_t len = sizeof(cliaddr);

    // Create UDP socket
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd < 0) {
        std::cerr << "Socket creation failed" << std::endl;
        return -1;
    }

    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = INADDR_ANY;
    servaddr.sin_port = htons(UDP_PORT);

    // Bind socket
    if (bind(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr)) < 0) {
        std::cerr << "Bind failed" << std::endl;
        close(sockfd);
        return -1;
    }

    while (true) {
        ssize_t recv_len = recvfrom(sockfd, buffer, BUFFER_SIZE, 0, (struct sockaddr *)&cliaddr, &len);
        if (recv_len < 0) {
            std::cerr << "Failed to receive data" << std::endl;
            break;
        }

        // Convert received data into OpenCV Mat
        std::vector<uchar> frame_data(buffer, buffer + recv_len);
        cv::Mat frame = cv::imdecode(frame_data, cv::IMREAD_COLOR);

        if (!frame.empty()) {
            cv::imshow("Stream", frame);
        }

        if (cv::waitKey(1) == 'q') {
            break;
        }
    }

    close(sockfd);
    cv::destroyAllWindows();
    return 0;
}
